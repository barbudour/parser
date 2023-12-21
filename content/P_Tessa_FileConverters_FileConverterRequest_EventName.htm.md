# FileConverterRequest.EventName - свойство
Алиас события, для которого выполняется предпросмотр. Значение используется
для вычисления хеша запроса. Список стандартных алиасов можно получить из
класса [Tessa.FileConverters.FileConverterEventNames].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string EventName { get; set; }
VB __Копировать
     Public Property EventName As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ EventName {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract EventName : string with get, set
    override EventName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterRequest.EventName](P_Tessa_FileConverters_IFileConverterRequest_EventName.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
