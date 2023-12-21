# AggregateEDSManager.VerifySignatureAsync - метод
Проверяет электронную подпись документа, возвращает признак успешной проверки
и текст ошибки, если проверка неуспешна.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<(bool success, string errorText)> VerifySignatureAsync(
    	byte[] encodedSignature,
    	ISignatureFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function VerifySignatureAsync ( 
    	encodedSignature As Byte(),
    	file As ISignatureFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (success As Boolean, errorText As String))
C++ __Копировать
     public:
    virtual ValueTask<ValueTuple<bool, String^>> VerifySignatureAsync(
    	array<unsigned char>^ encodedSignature, 
    	ISignatureFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract VerifySignatureAsync : 
            encodedSignature : byte[] * 
            file : ISignatureFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, string>> 
    override VerifySignatureAsync : 
            encodedSignature : byte[] * 
            file : ISignatureFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, string>> 
#### Параметры
encodedSignature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Файл подписи.
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
    Документ, который необходимо проверить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>  
Признак успешной проверки и текст ошибки, если проверка неуспешна.
#### Реализации
[IEDSManager.VerifySignatureAsync(Byte[], ISignatureFile,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_VerifySignatureAsync.htm)  
##  __См. также
#### Ссылки
[AggregateEDSManager -
](T_Tessa_Extensions_Default_Shared_EDS_AggregateEDSManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
