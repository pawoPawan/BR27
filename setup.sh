#!/bin/bash

# BR27 Website Setup Script
# Easily start, stop, and manage the local web server

PORT=8000
PID_FILE=".server.pid"
LOG_FILE=".server.log"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Function to check if server is running
is_running() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            return 0
        else
            rm -f "$PID_FILE"
            return 1
        fi
    fi
    return 1
}

# Function to start the server
start_server() {
    if is_running; then
        print_warning "Server is already running on port $PORT"
        print_info "Visit: http://localhost:$PORT"
        return 1
    fi

    print_info "Starting BR27 web server on port $PORT..."
    
    # Start Python HTTP server in background
    python3 -m http.server $PORT > "$LOG_FILE" 2>&1 &
    SERVER_PID=$!
    
    # Save PID
    echo $SERVER_PID > "$PID_FILE"
    
    # Wait a moment and check if it started successfully
    sleep 1
    
    if is_running; then
        print_success "Server started successfully!"
        print_success "Visit: http://localhost:$PORT"
        print_info "PID: $SERVER_PID"
        echo ""
        print_info "Commands:"
        echo "  ./setup.sh stop    - Stop the server"
        echo "  ./setup.sh status  - Check server status"
        echo "  ./setup.sh restart - Restart the server"
    else
        print_error "Failed to start server"
        rm -f "$PID_FILE"
        return 1
    fi
}

# Function to stop the server
stop_server() {
    if ! is_running; then
        print_warning "Server is not running"
        return 1
    fi

    PID=$(cat "$PID_FILE")
    print_info "Stopping server (PID: $PID)..."
    
    kill $PID 2>/dev/null
    
    # Wait for process to stop
    sleep 1
    
    if ! is_running; then
        rm -f "$PID_FILE"
        print_success "Server stopped successfully"
    else
        print_warning "Server did not stop gracefully, forcing..."
        kill -9 $PID 2>/dev/null
        rm -f "$PID_FILE"
        print_success "Server forcefully stopped"
    fi
}

# Function to check server status
check_status() {
    if is_running; then
        PID=$(cat "$PID_FILE")
        print_success "Server is running"
        print_info "PID: $PID"
        print_info "URL: http://localhost:$PORT"
        
        # Try to show server uptime
        if ps -p "$PID" -o etime= > /dev/null 2>&1; then
            UPTIME=$(ps -p "$PID" -o etime= | tr -d ' ')
            print_info "Uptime: $UPTIME"
        fi
    else
        print_warning "Server is not running"
        return 1
    fi
}

# Function to restart the server
restart_server() {
    print_info "Restarting server..."
    stop_server
    sleep 1
    start_server
}

# Function to open browser
open_browser() {
    if ! is_running; then
        print_error "Server is not running. Start it first with: ./setup.sh start"
        return 1
    fi
    
    URL="http://localhost:$PORT"
    print_info "Opening $URL in browser..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open "$URL"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open "$URL" 2>/dev/null || print_warning "Could not open browser automatically"
    else
        print_warning "Please open $URL manually in your browser"
    fi
}

# Function to show logs
show_logs() {
    if [ -f "$LOG_FILE" ]; then
        print_info "Server logs:"
        echo ""
        tail -n 20 "$LOG_FILE"
    else
        print_warning "No log file found"
    fi
}

# Function to clean up
cleanup() {
    print_info "Cleaning up temporary files..."
    rm -f "$PID_FILE" "$LOG_FILE"
    print_success "Cleanup complete"
}

# Function to show help
show_help() {
    echo ""
    echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║     BR27 Website Management Tool      ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
    echo ""
    echo "Usage: ./setup.sh [command]"
    echo ""
    echo "Commands:"
    echo "  start      Start the web server"
    echo "  stop       Stop the web server"
    echo "  restart    Restart the web server"
    echo "  status     Check if server is running"
    echo "  open       Open website in browser"
    echo "  logs       Show server logs"
    echo "  cleanup    Remove temporary files"
    echo "  help       Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./setup.sh start    # Start the server"
    echo "  ./setup.sh open     # Start server and open in browser"
    echo "  ./setup.sh stop     # Stop the server"
    echo ""
}

# Main script logic
main() {
    case "$1" in
        start)
            start_server
            ;;
        stop)
            stop_server
            ;;
        restart)
            restart_server
            ;;
        status)
            check_status
            ;;
        open)
            if ! is_running; then
                start_server
                sleep 1
            fi
            open_browser
            ;;
        logs)
            show_logs
            ;;
        cleanup)
            if is_running; then
                print_error "Please stop the server before cleanup"
                exit 1
            fi
            cleanup
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            if [ -z "$1" ]; then
                show_help
            else
                print_error "Unknown command: $1"
                show_help
                exit 1
            fi
            ;;
    esac
}

# Run main function
main "$@"

