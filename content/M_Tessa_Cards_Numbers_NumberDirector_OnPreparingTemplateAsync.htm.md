# NumberDirector.OnPreparingTemplateAsync - метод
Уведомляет о том, что карточка шаблона подготавливается к созданию по шаблону.
При этом может потребоваться очистить поля номеров, заданных в шаблоне. Обычно
выполняется на сервере на этапе AfterRequest после создания карточки, но перед
событием [Tessa.Cards.Numbers.NumberEventTypes.CreatingCard].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> OnPreparingTemplateAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function OnPreparingTemplateAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ OnPreparingTemplateAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract OnPreparingTemplateAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override OnPreparingTemplateAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработка события успешно выполнена; false, если обработка события
была отменена или при выполнении обработки возникли ошибки.
## __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
