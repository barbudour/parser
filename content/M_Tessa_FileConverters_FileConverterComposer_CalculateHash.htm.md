# FileConverterComposer.CalculateHash - метод
Вычисляет хеш запроса, который может использоваться при обращении к кэшу.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] CalculateHash(
    	IFileConverterRequest request
    )
VB __Копировать
     Public Function CalculateHash ( 
    	request As IFileConverterRequest
    ) As Byte()
C++ __Копировать
     public:
    virtual array<unsigned char>^ CalculateHash(
    	IFileConverterRequest^ request
    ) sealed
F# __Копировать
     abstract CalculateHash : 
            request : IFileConverterRequest -> byte[] 
    override CalculateHash : 
            request : IFileConverterRequest -> byte[] 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Вычисленный хеш от запроса.
#### Реализации
[IFileConverterComposer.CalculateHash(IFileConverterRequest)](M_Tessa_FileConverters_IFileConverterComposer_CalculateHash.htm)  
##  __См. также
#### Ссылки
[FileConverterComposer - ](T_Tessa_FileConverters_FileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
