# PageResultResponseControl.Cookie - свойство
The
[Cookie()](https://learn.microsoft.com/dotnet/api/system.directoryservices.protocols.pageresultresponsecontrol.cookie#system-
directoryservices-protocols-pageresultresponsecontrol-cookie) property
contains the page search cookie returned by the server.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] Cookie { get; }
VB __Копировать
     Public ReadOnly Property Cookie As Byte()
    	Get
C++ __Копировать
     public:
    property array<unsigned char>^ Cookie {
    	array<unsigned char>^ get ();
    }
F# __Копировать
     member Cookie : byte[] with get
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
The page search cookie returned by the server. If the cookie is empty, then
the paged search completed.
##  __См. также
#### Ссылки
[PageResultResponseControl -
](T_Tessa_Extensions_Platform_Server_AdSync_PageResultResponseControl.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
