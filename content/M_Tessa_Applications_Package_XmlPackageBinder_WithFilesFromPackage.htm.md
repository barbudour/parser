# XmlPackageBinder.WithFilesFromPackage - метод
Устанавливает признак необходимости загрузки информации о файлах из пакета.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public XmlPackageBinder WithFilesFromPackage(
    	bool fileLoading
    )
VB __Копировать
    <NotNullAttribute>
    Public Function WithFilesFromPackage ( 
    	fileLoading As Boolean
    ) As XmlPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    XmlPackageBinder^ WithFilesFromPackage(
    	bool fileLoading
    )
F# __Копировать
     [<NotNullAttribute>]
    member WithFilesFromPackage : 
            fileLoading : bool -> XmlPackageBinder 
#### Параметры
fileLoading [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак необходимости загрузки информации о файлах из пакета. 
#### Возвращаемое значение
[XmlPackageBinder](T_Tessa_Applications_Package_XmlPackageBinder.htm)  
Ссылка на построитель пакета.
## __Заметки
Действует только когда не был выставлен флаг загрузки фактичекой информации о
файлах с помощью
[WithFiles(Boolean)](M_Tessa_Applications_Package_XmlPackageBinder_WithFiles.htm).
##  __См. также
#### Ссылки
[XmlPackageBinder - ](T_Tessa_Applications_Package_XmlPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
