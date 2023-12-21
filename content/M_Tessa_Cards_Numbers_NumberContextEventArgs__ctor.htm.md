# NumberContextEventArgs - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberContextEventArgs(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    NumberContextEventArgs(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> NumberContextEventArgs
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу
##  __См. также
#### Ссылки
[NumberContextEventArgs - ](T_Tessa_Cards_Numbers_NumberContextEventArgs.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
