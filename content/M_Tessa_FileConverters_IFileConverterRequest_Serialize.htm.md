# IFileConverterRequest.Serialize - метод
Сериализует информацию в заданном хранилище для передачи в запускаемую
операцию.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IFileConverterRequest Serialize(
    	IDictionary<string, Object> storage
    )
VB __Копировать
     Function Serialize ( 
    	storage As IDictionary(Of String, Object)
    ) As IFileConverterRequest
C++ __Копировать
    IFileConverterRequest^ Serialize(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract Serialize : 
            storage : IDictionary<string, Object> -> IFileConverterRequest 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое будет содержать сериализованные данные.
#### Возвращаемое значение
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
