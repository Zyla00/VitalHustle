class AlertManager {
    constructor(defaultDuration = 5000) {
        this.notyf = new Notyf({
            duration: defaultDuration,
            position: {
                x: 'right',
                y: 'top'
            },
            dismissible: true,
            ripple: true,
            queue: true
        });
        this.defaultDuration = defaultDuration;
    }

    success(message, duration = this.defaultDuration) {
        this.notyf.success({message, duration});
    }

    error(message, duration = this.defaultDuration) {
        this.notyf.error({message, duration});
    }

    warning(message, duration = this.defaultDuration) {
        this.notyf.open({
            type: 'warning',
            message: message,
            duration: duration
        });
    }
}