# FileConverterRequest.FileTypeName - свойство
Имя типа преобразуемого файла, который указывается в запросе на конвертацию
CardGetFileContentRequest.FileTypeName, или null, если свойство не указывается
в запросе. От значения этого свойства зависит вычисление хеша запроса (и
идентификация похожих операций). Значение необязательно для заполнения, его
можно использовать для конвертации виртуальных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string FileTypeName { get; set; }
VB __Копировать
     Public Property FileTypeName As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ FileTypeName {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract FileTypeName : string with get, set
    override FileTypeName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterRequest.FileTypeName](P_Tessa_FileConverters_IFileConverterRequest_FileTypeName.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
