# ApplicationDownloadFlags - перечисление
Флаги, влияющие на скачивание приложений с веб-сервиса. Флаги проверяются
только на сервере и не учитываются при указании со стороны клиента.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum ApplicationDownloadFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration ApplicationDownloadFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class ApplicationDownloadFlags
F# __Копировать
     [<FlagsAttribute>]
    type ApplicationDownloadFlags
##  __Члены
None| 0|  Флаги не заданы.  
---|---|---  
PackageBinarySerialization| 1|  Использует бинарную сериализацию средствами
[ApplicationPackageWriter](T_Tessa_Applications_Synchronization_ApplicationPackageWriter.htm)
для передачи пакета приложения
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm) при
его скачивании. Флаг задействуется для обратной совместимости с предыдущими
версиями Tessa Applications.  
## __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
