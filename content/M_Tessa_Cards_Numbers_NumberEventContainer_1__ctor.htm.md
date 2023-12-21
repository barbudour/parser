# NumberEventContainer<T> \- конструктор
Создаёт экземпляр класса с указанием события, происходящего с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberEventContainer(
    	Func<INumberContext, CancellationToken, Task<T>> numberEventFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	numberEventFuncAsync As Func(Of INumberContext, CancellationToken, Task(Of T))
    )
C++ __Копировать
     public:
    NumberEventContainer(
    	Func<INumberContext^, CancellationToken, Task<T>^>^ numberEventFuncAsync
    )
F# __Копировать
     new : 
            numberEventFuncAsync : Func<INumberContext, CancellationToken, Task<'T>> -> NumberEventContainer
#### Параметры
numberEventFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[T](T_Tessa_Cards_Numbers_NumberEventContainer_1.htm)>>
     Обработчик события, происходящего с номером, который принимает в параметре контекст действия [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm), отличный от null, и возвращающее ссылочный результат действия. Если возвращается null, то действие считается неудачным. 
## __См. также
#### Ссылки
[NumberEventContainer<T> \-
](T_Tessa_Cards_Numbers_NumberEventContainer_1.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
