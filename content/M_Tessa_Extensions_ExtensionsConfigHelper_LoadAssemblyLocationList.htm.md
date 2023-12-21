# ExtensionsConfigHelper.LoadAssemblyLocationList - метод
Возвращает список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, располагающемся в указанной папке.
Конфигурационный файл должен иметь имя, заданное в константе
[ConfigFileName](F_Tessa_Extensions_ExtensionsConfigHelper_ConfigFileName.htm).
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<string> LoadAssemblyLocationList(
    	string folderPath,
    	SessionType sessionType,
    	List<string> pathToScanList,
    	ref List<string> referenceList
    )
VB __Копировать
     Public Shared Function LoadAssemblyLocationList ( 
    	folderPath As String,
    	sessionType As SessionType,
    	pathToScanList As List(Of String),
    	ByRef referenceList As List(Of String)
    ) As List(Of String)
C++ __Копировать
     public:
    static List<String^>^ LoadAssemblyLocationList(
    	String^ folderPath, 
    	SessionType sessionType, 
    	List<String^>^ pathToScanList, 
    	List<String^>^% referenceList
    )
F# __Копировать
     static member LoadAssemblyLocationList : 
            folderPath : string * 
            sessionType : SessionType * 
            pathToScanList : List<string> * 
            referenceList : List<string> byref -> List<string> 
#### Параметры
folderPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь до папки с плагинами.
sessionType [SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
    Тип сессии для регистрации расширений.
pathToScanList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Список папок, которые требуется дополнительно просканировать на наличие сборок. Метод добавляет в этот список те папки, которые указаны в конфигурационном файле. 
referenceList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Список полных путей до сборок, которые необходимо подключить, прежде чем плагины будут загружены, или null, если таких сборок нет. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, или пустой список, если такие указания отсутствовали,
конфигурационный файл отсутствует или возникли проблемы с его разбором.
## __См. также
#### Ссылки
[ExtensionsConfigHelper - ](T_Tessa_Extensions_ExtensionsConfigHelper.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
