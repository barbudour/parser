# Check - класс
Вспомогательные методы для проверки некоторых стандартных условий.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class Check
VB __Копировать
     Public NotInheritable Class Check
C++ __Копировать
     public ref class Check abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type Check = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Check
##  __Методы
[ArgumentNotNull](M_Tessa_Platform_Check_ArgumentNotNull.htm)|  Throws
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)
if the given argument is null.  
---|---  
[ArgumentNotNullOrEmpty](M_Tessa_Platform_Check_ArgumentNotNullOrEmpty.htm)|
Throws an exception if the tested string argument is null or the empty string.  
[ArgumentNotNullOrWhiteSpace](M_Tessa_Platform_Check_ArgumentNotNullOrWhiteSpace.htm)|  
[ObjectNotSealed](M_Tessa_Platform_Check_ObjectNotSealed.htm)|  Выбрасывает
исключение
[ObjectSealedException](T_Tessa_Platform_ObjectSealedException.htm), если
заданный объект был защищён от изменений.  
[Type<T>](M_Tessa_Platform_Check_Type__1.htm)|  Проверяет, что тип заданного
объекта равен T.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
