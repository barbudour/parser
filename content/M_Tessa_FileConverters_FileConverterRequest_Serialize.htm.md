# FileConverterRequest.Serialize - метод
Сериализует информацию в заданном хранилище для передачи в запускаемую
операцию.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual IFileConverterRequest Serialize(
    	IDictionary<string, Object> storage
    )
VB __Копировать
     Public Overridable Function Serialize ( 
    	storage As IDictionary(Of String, Object)
    ) As IFileConverterRequest
C++ __Копировать
     public:
    virtual IFileConverterRequest^ Serialize(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract Serialize : 
            storage : IDictionary<string, Object> -> IFileConverterRequest 
    override Serialize : 
            storage : IDictionary<string, Object> -> IFileConverterRequest 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое будет содержать сериализованные данные.
#### Возвращаемое значение
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[IFileConverterRequest.Serialize(IDictionary<String,
Object>)](M_Tessa_FileConverters_IFileConverterRequest_Serialize.htm)  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
