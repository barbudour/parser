# IFileConverterRequest.FileTypeName - свойство
Имя типа преобразуемого файла, который указывается в запросе на конвертацию
CardGetFileContentRequest.FileTypeName, или null, если свойство не указывается
в запросе. От значения этого свойства зависит вычисление хеша запроса (и
идентификация похожих операций). Значение необязательно для заполнения, его
можно использовать для конвертации виртуальных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string FileTypeName { get; set; }
VB __Копировать
     Property FileTypeName As String
    	Get
    	Set
C++ __Копировать
    property String^ FileTypeName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract FileTypeName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
