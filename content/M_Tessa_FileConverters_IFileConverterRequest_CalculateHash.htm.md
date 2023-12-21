# IFileConverterRequest.CalculateHash - метод
Вычисляет хеш операции по конвертации для данного запроса, по которому, в том
числе, выполняется сравнение операций и их результатов в кэше. По умолчанию
учитываются значения свойств VersionID, EventName, OutputFormat и Parameters.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     byte[] CalculateHash(
    	ISignatureProvider signatureProvider
    )
VB __Копировать
     Function CalculateHash ( 
    	signatureProvider As ISignatureProvider
    ) As Byte()
C++ __Копировать
    array<unsigned char>^ CalculateHash(
    	ISignatureProvider^ signatureProvider
    )
F# __Копировать
     abstract CalculateHash : 
            signatureProvider : ISignatureProvider -> byte[] 
#### Параметры
signatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm)
    Объект, используемый для вычисления хеша по данным запроса.
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Вычисленный хеш операции по конвертации.
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
