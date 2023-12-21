# FastReflectionCache - класс
Кэш делегатов доступа к членам классов через деревья выражений
## __Definition
 **Пространство имён:**
[Tessa.Platform.Reflection](N_Tessa_Platform_Reflection.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FastReflectionCache
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class FastReflectionCache
C++ __Копировать
    [ExtensionAttribute]
    public ref class FastReflectionCache abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type FastReflectionCache = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FastReflectionCache
##  __Методы
[AddEventHandler<T>](M_Tessa_Platform_Reflection_FastReflectionCache_AddEventHandler__1.htm)|  
---|---  
[AsEnumerable<T>](M_Tessa_Platform_Reflection_FastReflectionCache_AsEnumerable__1.htm)|
Возвращает объект obj в виде перечисления  
[RemoveEventHandler<T>](M_Tessa_Platform_Reflection_FastReflectionCache_RemoveEventHandler__1.htm)|  
[TryGetAccessor<TInstance,
TValue>](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetAccessor__2.htm)|
Возвращает объект предоставляющий доступ к полю или свойству  
[TryGetFieldGetter<TResult>(Object,
String)](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetFieldGetter__1.htm)|  
[TryGetFieldGetter<TClass,
TResult>(String)](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetFieldGetter__2.htm)|
Возвращает функцию доступа к полю или свойству объекта типа TClass, имеющему
наименование fieldName и тип TResult  
[TryGetFieldSetter<TClass,
TValue>](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetFieldSetter__2.htm)|
Возвращает функцию доступа к полю или свойству объекта типа TClass для записи
элемента, имеющего наименование fieldName и тип TValue  
[TryGetMethod<TMethod>(String,
BindingFlags)](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetMethod__1_1.htm)|
Возвращает функцию осуществляющую вызов функции methodName  
[TryGetMethod<TMethod>(Object, String,
BindingFlags)](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetMethod__1.htm)|
Возвращает функцию осуществляющую вызов функции methodName  
[TryGetPrivateMethod<TMethod>](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetPrivateMethod__1.htm)|
Возвращает функцию осуществляющую вызов приватной функции methodName  
[TryGetPublicMethod<TMethod>](M_Tessa_Platform_Reflection_FastReflectionCache_TryGetPublicMethod__1.htm)|
Возвращает функцию осуществляющую вызов публичной функции methodName  
##  __См. также
#### Ссылки
[Tessa.Platform.Reflection - пространство
имён](N_Tessa_Platform_Reflection.htm)
