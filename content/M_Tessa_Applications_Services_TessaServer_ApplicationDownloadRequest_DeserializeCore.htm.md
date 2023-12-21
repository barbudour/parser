# ApplicationDownloadRequest.DeserializeCore - метод
Выполняет десериализацию полей объекта из заданного хранилища.
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void DeserializeCore(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overrides Sub DeserializeCore ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void DeserializeCore(
    	Dictionary<String^, Object^>^ storage
    ) override
F# __Копировать
     abstract DeserializeCore : 
            storage : Dictionary<string, Object> -> unit 
    override DeserializeCore : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, из которого десериализуется объект.
#### Возвращаемое значение
Десериализованный объект.
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[ApplicationDownloadRequest -
](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadRequest.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
