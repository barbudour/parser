# InheritableRetainingScope<T> \- класс
Класс, позволяющий создавать наследуемые области видимости для объекта
заданного типа, которые могут "удерживаться" посредством области
[ScopeHolderContext](T_Tessa_Platform_Scopes_ScopeHolderContext.htm). Также
область видимости существует в контексте текущего контекста вызова
ExecutionContext, т.е. он "пробрасывается" при выполнении асинхронных действий
async/await. Наследуемость определяется тем, что во вложенных областях
видимости возвращается тот же объект, что был создан для внешней области
видимости.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class InheritableRetainingScope<T>
    where T : class
VB __Копировать
     Public NotInheritable Class InheritableRetainingScope(Of T As Class)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class InheritableRetainingScope abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type InheritableRetainingScope<'T when 'T : not struct> = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ InheritableRetainingScope<T>
#### Параметры типа
T
    Ссылочный тип значения, область видимости которого определяется.
##  __Свойства
[Value](P_Tessa_Platform_Scopes_InheritableRetainingScope_1_Value.htm)|
Значение, область видимости которого определяется.  
---|---  
##  __Методы
[Create](M_Tessa_Platform_Scopes_InheritableRetainingScope_1_Create.htm)|
Создаёт область видимости для значения в текущем потоке. Указывается функция,
создающая значение при первом обращении или при первом вызове метода в
зависимости от isLazy. Разрешены вложенные области видимости. Если созданный
функцией объект реализует
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), то
при выходе за внешнюю область видимости в текущем потоке объект будет
освобождён вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose).  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
