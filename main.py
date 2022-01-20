from CuentaBancaria import CuentaBancaria

cuenta_1 = CuentaBancaria()
cuenta_2 = CuentaBancaria()

cuenta_1.deposito(100).deposito(300).deposito(50).retiro(70).generar_interes().mostrar_info_cuenta()

cuenta_2.deposito(1000).deposito(70).retiro(200).retiro(20).retiro(345).retiro(77).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_info_cuenta()

