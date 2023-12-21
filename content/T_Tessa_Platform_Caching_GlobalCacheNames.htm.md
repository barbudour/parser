# GlobalCacheNames - класс
Глобальный список имён экземпляров кэша, являющихся наследниками класса
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class GlobalCacheNames
VB __Копировать
     Public NotInheritable Class GlobalCacheNames
C++ __Копировать
     public ref class GlobalCacheNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type GlobalCacheNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalCacheNames
##  __Заметки
Указанные здесь имена не должны быть заняты для общих нужд в экземплярах,
синхронизация для которых осуществляется между любыми наследниками класса
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm). Если
синхронизация осуществляется для конкретного типа экземпляра, то это
ограничение не применимо.
## __Поля
[Default](F_Tessa_Platform_Caching_GlobalCacheNames_Default.htm)|  Имя
экземпляра кэша по умолчанию.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
