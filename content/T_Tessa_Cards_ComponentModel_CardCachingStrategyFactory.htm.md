# CardCachingStrategyFactory - класс
Фабрика, создающая стратегии кэширования для компонентов карточки по заданному
типу.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardCachingStrategyFactory
VB __Копировать
     Public NotInheritable Class CardCachingStrategyFactory
C++ __Копировать
     public ref class CardCachingStrategyFactory abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardCachingStrategyFactory = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardCachingStrategyFactory
##  __Методы
[CreateGetStrategy](M_Tessa_Cards_ComponentModel_CardCachingStrategyFactory_CreateGetStrategy.htm)|
Создаёт стратегию кэширования объектов для операции по загрузке карточки.
Обращение к любой созданной стратегии потокобезопасно.  
---|---  
[CreateNewStrategy](M_Tessa_Cards_ComponentModel_CardCachingStrategyFactory_CreateNewStrategy.htm)|
Создаёт стратегию кэширования объектов для операции по созданию карточки.
Обращение к любой созданной стратегии потокобезопасно.  
[CreateStoreStrategy](M_Tessa_Cards_ComponentModel_CardCachingStrategyFactory_CreateStoreStrategy.htm)|
Создаёт стратегию кэширования объектов для операции по сохранению карточки.
Обращение к любой созданной стратегии потокобезопасно.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
