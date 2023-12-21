# FileConverterRequest.Deserialize - метод
Десериализует информацию из заданного хранилища в свойства текущего объекта.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual IFileConverterRequest Deserialize(
    	IDictionary<string, Object> storage
    )
VB __Копировать
     Public Overridable Function Deserialize ( 
    	storage As IDictionary(Of String, Object)
    ) As IFileConverterRequest
C++ __Копировать
     public:
    virtual IFileConverterRequest^ Deserialize(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract Deserialize : 
            storage : IDictionary<string, Object> -> IFileConverterRequest 
    override Deserialize : 
            storage : IDictionary<string, Object> -> IFileConverterRequest 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое содержит сериализованные данные.
#### Возвращаемое значение
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[IFileConverterRequest.Deserialize(IDictionary<String,
Object>)](M_Tessa_FileConverters_IFileConverterRequest_Deserialize.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
