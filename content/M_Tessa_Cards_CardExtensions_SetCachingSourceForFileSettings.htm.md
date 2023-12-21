# CardExtensions.SetCachingSourceForFileSettings - метод
Устанавливает в качестве источника настроек
[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm) для зарегистрированного
объекта [ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm).
Привязывает кэш к параметрам лицензии
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm), если этот
объект зарегистрирован. Не выполняет действий, если хотя бы одна из
зависимостей [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm) или
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm) не
зарегистрированы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer SetCachingSourceForFileSettings(
    	this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetCachingSourceForFileSettings ( 
    	container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ SetCachingSourceForFileSettings(
    	IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetCachingSourceForFileSettings : 
            container : IUnityContainer -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер Unity.
#### Возвращаемое значение
IUnityContainer  
Контейнер Unity container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
