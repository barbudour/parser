# ExceptionHandlingMode - перечисление
Режим обработки исключений, возникающий в методах расширений. Может быть
изменён в т.ч. в методе
[NotifyException(IExtensionStrategyContext)](M_Tessa_Extensions_IExtensionTraceListener_NotifyException.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ExceptionHandlingMode
VB __Копировать
     Public Enumeration ExceptionHandlingMode
C++ __Копировать
     public enum class ExceptionHandlingMode
F# __Копировать
     type ExceptionHandlingMode
##  __Члены
Rethrow| 0|  Исключение не логируется и выбрасывается наружу как
необработанное. Если один из методов расширений упал с необработанным
исключением, то падает вся цепочка. Это поведение по умолчанию.  
---|---|---  
Log| 1|  Исключение логируется и не выбрасывается наружу. Если метод
расширения упал с необработанным исключением, то цепочка расширений продолжает
выполняться.  
Ignore| 2|  Исключение игнорируется, т.е. не логируется и не выбрасывается
наружу. Если метод расширения упал с необработанным исключением, то цепочка
расширений продолжает выполняться.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
