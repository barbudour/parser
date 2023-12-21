# INumberDirector.GetDigestAsync - метод
Возвращает Digest карточки по её номерам.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<string> GetDigestAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetDigestAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
    Task<String^>^ GetDigestAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetDigestAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Digest карточки, полученный по её номерам, или null, если получить Digest не
удалось.
## __См. также
#### Ссылки
[INumberDirector - ](T_Tessa_Cards_Numbers_INumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
