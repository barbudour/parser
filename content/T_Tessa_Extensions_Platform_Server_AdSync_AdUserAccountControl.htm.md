# AdUserAccountControl - перечисление
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum AdUserAccountControl
VB __Копировать
    <FlagsAttribute>
    Public Enumeration AdUserAccountControl
C++ __Копировать
    [FlagsAttribute]
    public enum class AdUserAccountControl
F# __Копировать
     [<FlagsAttribute>]
    type AdUserAccountControl
##  __Члены
NONE| 0|  Пустой список  
---|---|---  
SCRIPT| 1|  Запуск сценария входа.  
ACCOUNTDISABLE| 2|  Отключение учетной записи пользователя.  
HOMEDIR_REQUIRED| 8|  Требуется домашняя папка.  
LOCKOUT| 16|  LOCKOUT  
PASSWD_NOTREQD| 32|  Пароль не требуется.  
PASSWD_CANT_CHANGE| 64|  Пользователь не может изменить пароль.  
ENCRYPTED_TEXT_PWD_ALLOWED| 128|  Пользователь может отправить зашифрованный
пароль.  
TEMP_DUPLICATE_ACCOUNT| 256|  Учетная запись для пользователей, чьи основные
учетные записи хранятся в другом домене.  
NORMAL_ACCOUNT| 512|  Тип учетной записи, используемой по умолчанию и
представляющей обычного пользователя.  
INTERDOMAIN_TRUST_ACCOUNT| 2,048|  Разрешение доверять учетную запись домену
системы, доверяющему другим доменам.  
WORKSTATION_TRUST_ACCOUNT| 4,096|  Учетная запись для компьютера,
использующего Microsoft Windows NT 4.0 Workstation, Microsoft Windows NT 4.0
Server, Microsoft Windows 2000 Professional или Windows 2000 Server и
являющегося членом данного домена.  
SERVER_TRUST_ACCOUNT| 8,192|  Учетная запись для контроллера домена,
являющегося членом данного домена.  
DONT_EXPIRE_PASSWORD| 65,536|  Представляется пароль, срок действия которого
не истекает для данной учетной записи.  
MNS_LOGON_ACCOUNT| 131,072|  Учетная запись входа MNS.  
SMARTCARD_REQUIRED| 262,144|  Пользователь может осуществить вход только с
использованием смарт-карты.  
TRUSTED_FOR_DELEGATION| 524,288|  Учетной записи службы (пользователя или
компьютера), под которой выполняется служба, доверяется делегирование
Kerberos. Любая подобная служба может олицетворять клиента, запрашивающего
службу.  
NOT_DELEGATED| 1,048,576|  Контекст безопасности пользователя не делегируется
службе, даже если учетной записи службы доверено делегирование Kerberos.  
USE_DES_KEY_ONLY| 2,097,152|  (Windows 2000/Windows Server 2003) Участник
может использовать только тип шифрования DES для ключей.  
DONT_REQ_PREAUTH| 4,194,304|  (Windows 2000/Windows Server 2003) Данная
учетная запись не требует предварительной проверки Kerberos для входа.  
PASSWORD_EXPIRED| 8,388,608|  (Windows 2000/Windows Server 2003) Срок действия
пароля пользователя истек.  
TRUSTED_TO_AUTH_FOR_DELEGATION| 16,777,216|  (Windows 2000/Windows Server
2003) Данной учетной записи разрешено делегирование.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
