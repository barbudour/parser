# AdSettings.Port - свойство
Порт, по которому выполняется подключение. Если значение равно 0 или
отрицательное число, то используется порт по умолчанию в зависимости от
свойства [ILdapSettings.UseSsl]: если true, то порт 636; если false, то порт
389.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int Port { get; }
VB __Копировать
     Public ReadOnly Property Port As Integer
    	Get
C++ __Копировать
     public:
    virtual property int Port {
    	int get () sealed;
    }
F# __Копировать
     abstract Port : int with get
    override Port : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
#### Реализации
[ILdapSettings.Port](P_Tessa_Platform_ILdapSettings_Port.htm)  
##  __См. также
#### Ссылки
[AdSettings - ](T_Tessa_Extensions_Platform_Server_AdSync_AdSettings.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
