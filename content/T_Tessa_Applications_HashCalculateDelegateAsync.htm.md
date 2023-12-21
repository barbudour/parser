# HashCalculateDelegateAsync - делегат
Осуществляет расчет контрольной суммы для потока
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<byte[]> HashCalculateDelegateAsync(
    	[CanBeNullAttribute] Stream stream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function HashCalculateDelegateAsync ( 
    	<CanBeNullAttribute> stream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public delegate Task<array<unsigned char>^>^ HashCalculateDelegateAsync(
    	[CanBeNullAttribute] Stream^ stream, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type HashCalculateDelegateAsync = 
        delegate of 
            [<CanBeNullAttribute>] stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]>
#### Параметры
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток для которого производится расчет контрольной суммы
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>  
Контрольная сумма или null, если поток пуст или равен null
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
