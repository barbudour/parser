# IFileConverterRequest.EventName - свойство
Алиас события, для которого выполняется предпросмотр. Значение используется
для вычисления хеша запроса. Список стандартных алиасов можно получить из
класса [Tessa.FileConverters.FileConverterEventNames].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string EventName { get; set; }
VB __Копировать
     Property EventName As String
    	Get
    	Set
C++ __Копировать
    property String^ EventName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract EventName : string with get, set
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
