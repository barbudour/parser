# SingletonNotFoundInCacheException.GetObjectData - метод
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override void GetObjectData(
    	SerializationInfo info,
    	StreamingContext context
    )
VB __Копировать
     Public Overrides Sub GetObjectData ( 
    	info As SerializationInfo,
    	context As StreamingContext
    )
C++ __Копировать
     public:
    virtual void GetObjectData(
    	SerializationInfo^ info, 
    	StreamingContext context
    ) override
F# __Копировать
     abstract GetObjectData : 
            info : SerializationInfo * 
            context : StreamingContext -> unit 
    override GetObjectData : 
            info : SerializationInfo * 
            context : StreamingContext -> unit 
#### Параметры
info
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
    Объект, в который будут записаны сериализованные данные создаваемого объекта.
context
[StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)
    Контекст сериализации.
#### Реализации
[ISerializable.GetObjectData(SerializationInfo,
StreamingContext)](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable.getobjectdata#system-
runtime-serialization-iserializable-getobjectdata\(system-runtime-
serialization-serializationinfo-system-runtime-serialization-
streamingcontext\))  
##  __См. также
#### Ссылки
[SingletonNotFoundInCacheException -
](T_Tessa_Cards_Caching_SingletonNotFoundInCacheException.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
