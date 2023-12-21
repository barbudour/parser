# FileConverterRequest.CalculateHash - метод
Вычисляет хеш операции по конвертации для данного запроса, по которому, в том
числе, выполняется сравнение операций и их результатов в кэше. По умолчанию
учитываются значения свойств VersionID, EventName, OutputFormat и Parameters.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] CalculateHash(
    	ISignatureProvider signatureProvider
    )
VB __Копировать
     Public Function CalculateHash ( 
    	signatureProvider As ISignatureProvider
    ) As Byte()
C++ __Копировать
     public:
    virtual array<unsigned char>^ CalculateHash(
    	ISignatureProvider^ signatureProvider
    ) sealed
F# __Копировать
     abstract CalculateHash : 
            signatureProvider : ISignatureProvider -> byte[] 
    override CalculateHash : 
            signatureProvider : ISignatureProvider -> byte[] 
#### Параметры
signatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm)
    Объект, используемый для вычисления хеша по данным запроса.
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Вычисленный хеш операции по конвертации.
#### Реализации
[IFileConverterRequest.CalculateHash(ISignatureProvider)](M_Tessa_FileConverters_IFileConverterRequest_CalculateHash.htm)  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
