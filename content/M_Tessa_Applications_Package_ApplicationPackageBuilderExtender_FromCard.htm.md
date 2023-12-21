# ApplicationPackageBuilderExtender.FromCard - метод
Создает объект осуществляющий формирование пакета приложения из строки
представления
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static CardApplicationPackageBinder FromCard(
    	[NotNullAttribute] this IPackageBinderFactory binderFactory,
    	[CanBeNullAttribute] Card card = null
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function FromCard ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory,
    	<CanBeNullAttribute> Optional card As Card = Nothing
    ) As CardApplicationPackageBinder
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static CardApplicationPackageBinder^ FromCard(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory, 
    	[CanBeNullAttribute] Card^ card = nullptr
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member FromCard : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory * 
            [<CanBeNullAttribute>] ?card : Card 
    (* Defaults:
            let _card = defaultArg card null
    *)
    -> CardApplicationPackageBinder 
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Фабрика создания объекта формирования пакета приложения 
card [Card](T_Tessa_Cards_Card.htm) (Optional)
     Карточка из которой будет формироваться пакет приложения 
#### Возвращаемое значение
[CardApplicationPackageBinder](T_Tessa_Applications_Package_CardApplicationPackageBinder.htm)  
Объект осуществляющий формирование пакета приложения
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ApplicationPackageBuilderExtender -
](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
