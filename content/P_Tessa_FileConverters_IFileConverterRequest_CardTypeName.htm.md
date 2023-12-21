# IFileConverterRequest.CardTypeName - свойство
Имя типа карточки с преобразуемым файлом, который указывается в запросе на
конвертацию CardGetFileContentRequest.CardTypeName, или null, если свойство не
указывается в запросе. От значения этого свойства не зависит вычисление хеша
запроса (и идентификация похожих операций). Значение необязательно для
заполнения, его можно использовать для конвертации виртуальных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string CardTypeName { get; set; }
VB __Копировать
     Property CardTypeName As String
    	Get
    	Set
C++ __Копировать
    property String^ CardTypeName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract CardTypeName : string with get, set
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
