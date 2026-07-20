package com.laborlaw.ragkbdemo.exception;

/**
 * Raised when a request to an admin endpoint does not provide a valid token.
 */
public class AdminAuthException extends RuntimeException {

    public AdminAuthException(String message) {
        super(message);
    }
}
