# CardApplicationPackageBinder.Source(Func<Task<Card>>) - метод
Устанавливает в качестве источника карточку получаемую в результате выполнения
cardFuncAsync
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public CardApplicationPackageBinder Source(
    	[NotNullAttribute] Func<Task<Card>> cardFuncAsync
    )
VB __Копировать
    <NotNullAttribute>
    Public Function Source ( 
    	<NotNullAttribute> cardFuncAsync As Func(Of Task(Of Card))
    ) As CardApplicationPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    CardApplicationPackageBinder^ Source(
    	[NotNullAttribute] Func<Task<Card^>^>^ cardFuncAsync
    )
F# __Копировать
     [<NotNullAttribute>]
    member Source : 
            [<NotNullAttribute>] cardFuncAsync : Func<Task<Card>> -> CardApplicationPackageBinder 
#### Параметры
cardFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Card](T_Tessa_Cards_Card.htm)>>
     Функция возвращающая карточку приложения 
#### Возвращаемое значение
[CardApplicationPackageBinder](T_Tessa_Applications_Package_CardApplicationPackageBinder.htm)  
Ссылка на себя
## __См. также
#### Ссылки
[CardApplicationPackageBinder -
](T_Tessa_Applications_Package_CardApplicationPackageBinder.htm)
[Source -
перегрузка](Overload_Tessa_Applications_Package_CardApplicationPackageBinder_Source.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
