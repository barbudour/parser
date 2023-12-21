# ApplicationHostConnectionInfo.InstanceName - свойство
Имя экземпляра сервера для подключения. Если равно null или пустой строке, то
используется текущее имя экземпляра в настройках. Укажите
[DefaultLegacyInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultLegacyInstanceName.htm)
для подключения к серверам 2.x.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string InstanceName { get; set; }
VB __Копировать
     Public Property InstanceName As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ InstanceName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member InstanceName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
