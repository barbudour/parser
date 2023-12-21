# InitializationAddHandlerMode - перечисление
Способ добавления обработчика в поток инициализации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum InitializationAddHandlerMode
VB __Копировать
     Public Enumeration InitializationAddHandlerMode
C++ __Копировать
     public enum class InitializationAddHandlerMode
F# __Копировать
     type InitializationAddHandlerMode
##  __Члены
SkipIfExists| 0|  Не добавлять обработчик, если он уже существует.  
---|---|---  
ThrowIfExists| 1|  Выбросить исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception),
если обработчик уже существует.  
Overwrite| 2|  Перезаписать существующий обработчик.  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
