# HashHelper.CalculateHashAsync - метод
Осуществляет расчет контрольной суммы для потока stream
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<byte[]> CalculateHashAsync(
    	[NotNullAttribute] ISignatureProvider signatureProvider,
    	[CanBeNullAttribute] Stream stream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CalculateHashAsync ( 
    	<NotNullAttribute> signatureProvider As ISignatureProvider,
    	<CanBeNullAttribute> stream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public:
    static Task<array<unsigned char>^>^ CalculateHashAsync(
    	[NotNullAttribute] ISignatureProvider^ signatureProvider, 
    	[CanBeNullAttribute] Stream^ stream, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CalculateHashAsync : 
            [<NotNullAttribute>] signatureProvider : ISignatureProvider * 
            [<CanBeNullAttribute>] stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
#### Параметры
signatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm)
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
     Поток для которого осуществляется расчет контрольной суммы 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>  
Контрольная сумма или null, если расчет не возможен
## __См. также
#### Ссылки
[HashHelper - ](T_Tessa_Applications_HashHelper.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
