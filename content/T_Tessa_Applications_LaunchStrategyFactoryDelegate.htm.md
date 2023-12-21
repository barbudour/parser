# LaunchStrategyFactoryDelegate - делегат
Делегат экземпляры которого осуществляют создание стратегии запуска приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IApplicationLaunchingStrategy LaunchStrategyFactoryDelegate(
    	[NotNullAttribute] IApplicationModel applicationModel
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function LaunchStrategyFactoryDelegate ( 
    	<NotNullAttribute> applicationModel As IApplicationModel
    ) As IApplicationLaunchingStrategy
C++ __Копировать
    [NotNullAttribute]
    public delegate IApplicationLaunchingStrategy^ LaunchStrategyFactoryDelegate(
    	[NotNullAttribute] IApplicationModel^ applicationModel
    )
F# __Копировать
     [<NotNullAttribute>]
    type LaunchStrategyFactoryDelegate = 
        delegate of 
            [<NotNullAttribute>] applicationModel : IApplicationModel -> IApplicationLaunchingStrategy
#### Параметры
applicationModel
[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)
     Модель приложения 
#### Возвращаемое значение
[IApplicationLaunchingStrategy](T_Tessa_Applications_IApplicationLaunchingStrategy.htm)  
Стратегия запуска приложения
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
