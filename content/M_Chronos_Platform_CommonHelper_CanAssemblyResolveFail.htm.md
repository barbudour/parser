# CommonHelper.CanAssemblyResolveFail - метод
Возвращает признак того, что не следует писать в лог при ошибке загрузки
сборки. Сборка "Serilog" пытается загрузиться через библиотеку "Quartz" при
сканировании доступных средств логирование, и это совершенно нормально, что
загрузить её не получается. Сборка "System.Data.SqlClient" пытается
загрузиться через библиотеку "linq2db", и это нормально, что загрузить её не
получается. Сборка "Microsoft.SqlServer.Types" пытается загрузиться через
библиотеку "linq2db" при соединении с базой SQL Server для поддержки spatial-
типов, которые у нас не используются. Ошибка загрузки игнорируется. Сборка
"StackExchange.Redis" пытается загрузить
"Microsoft.WindowsAzure.ServiceRuntime", и загружать её не требуется, т.к.
подключение к Azure для Redis не используется.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CanAssemblyResolveFail(
    	AssemblyName assemblyName
    )
VB __Копировать
     Public Shared Function CanAssemblyResolveFail ( 
    	assemblyName As AssemblyName
    ) As Boolean
C++ __Копировать
     public:
    static bool CanAssemblyResolveFail(
    	AssemblyName^ assemblyName
    )
F# __Копировать
     static member CanAssemblyResolveFail : 
            assemblyName : AssemblyName -> bool 
#### Параметры
assemblyName
[AssemblyName](https://learn.microsoft.com/dotnet/api/system.reflection.assemblyname)
    Имя загружаемой сборки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если не следует писать в лог при ошибке загрузки сборки; false в
противном случае.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
