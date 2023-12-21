# TessaExpressionHelper - класс
Вспомогательные методы для взаимодействия с выражениями LINQ.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaExpressionHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class TessaExpressionHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class TessaExpressionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type TessaExpressionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaExpressionHelper
##  __Методы
[CompileGetter<T>(PropertyInfo)](M_Tessa_Platform_TessaExpressionHelper_CompileGetter__1.htm)|
Компилирует функцию, возвращающую значение свойства для заданного в параметре
объекта.  
---|---  
[CompileGetter<TObject, TProperty>(TObject, Expression<Func<TObject,
TProperty>>)](M_Tessa_Platform_TessaExpressionHelper_CompileGetter__2.htm)|
Компилирует функцию, которая возвращает значение свойства заданного объекта.  
[CompileSetter<T>(PropertyInfo)](M_Tessa_Platform_TessaExpressionHelper_CompileSetter__1.htm)|
Компилирует метод, устанавливающий значение свойства для заданного в первом
параметре объекта на заданное во втором параметре значение.  
[CompileSetter<TObject, TProperty>(TObject, Expression<Func<TObject,
TProperty>>)](M_Tessa_Platform_TessaExpressionHelper_CompileSetter__2.htm)|
Компилирует метод, который устанавливает значение свойства заданого объекта.  
[GetFieldAccessor<TTarget,
TFieldValue>](M_Tessa_Platform_TessaExpressionHelper_GetFieldAccessor__2.htm)|
Компилирует и возвращает функцию, получающую поле объекта с указанным именем.
Поле может быть приватным.  
[GetPropertyName<TObject,
TProperty>](M_Tessa_Platform_TessaExpressionHelper_GetPropertyName__2.htm)|
Возвращает имя свойства, запрашиваемого у объекта в заданном выражении.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
