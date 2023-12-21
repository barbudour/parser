# IFileConverterComposer.CalculateHash - метод
Вычисляет хеш запроса, который может использоваться при обращении к кэшу.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     byte[] CalculateHash(
    	IFileConverterRequest request
    )
VB __Копировать
     Function CalculateHash ( 
    	request As IFileConverterRequest
    ) As Byte()
C++ __Копировать
    array<unsigned char>^ CalculateHash(
    	IFileConverterRequest^ request
    )
F# __Копировать
     abstract CalculateHash : 
            request : IFileConverterRequest -> byte[] 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Вычисленный хеш от запроса.
##  __См. также
#### Ссылки
[IFileConverterComposer - ](T_Tessa_FileConverters_IFileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
