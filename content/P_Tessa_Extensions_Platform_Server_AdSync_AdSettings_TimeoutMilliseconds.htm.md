# AdSettings.TimeoutMilliseconds - свойство
Таймаут подключения в миллисекундах. Если значение равно 0 или отрицательное
число, то используется таймаут по умолчанию в зависимости от сервера LDAP
(обычно около 5 секунд).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int TimeoutMilliseconds { get; }
VB __Копировать
     Public ReadOnly Property TimeoutMilliseconds As Integer
    	Get
C++ __Копировать
     public:
    virtual property int TimeoutMilliseconds {
    	int get () sealed;
    }
F# __Копировать
     abstract TimeoutMilliseconds : int with get
    override TimeoutMilliseconds : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
#### Реализации
[ILdapSettings.TimeoutMilliseconds](P_Tessa_Platform_ILdapSettings_TimeoutMilliseconds.htm)  
##  __См. также
#### Ссылки
[AdSettings - ](T_Tessa_Extensions_Platform_Server_AdSync_AdSettings.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
