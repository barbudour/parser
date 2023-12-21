# XmlPackageBinder.WithFiles - метод
Устанавливает признак необходимости выполнения загрузки фактической информации
о файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public XmlPackageBinder WithFiles(
    	bool fileLoading
    )
VB __Копировать
    <NotNullAttribute>
    Public Function WithFiles ( 
    	fileLoading As Boolean
    ) As XmlPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    XmlPackageBinder^ WithFiles(
    	bool fileLoading
    )
F# __Копировать
     [<NotNullAttribute>]
    member WithFiles : 
            fileLoading : bool -> XmlPackageBinder 
#### Параметры
fileLoading [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак необходимости загрузки фактической информации о файлах. 
#### Возвращаемое значение
[XmlPackageBinder](T_Tessa_Applications_Package_XmlPackageBinder.htm)  
Ссылка на построитель пакета.
## __Заметки
Выполняет загрузку фактической информации о файлах путём перечисления всех
файлов каталога в котором текущий пакет с информацией о приложении.
##  __См. также
#### Ссылки
[XmlPackageBinder - ](T_Tessa_Applications_Package_XmlPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
