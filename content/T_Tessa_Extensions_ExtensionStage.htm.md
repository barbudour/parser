# ExtensionStage - перечисление
Этап выполнения расширения в цепочке расширений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ExtensionStage
VB __Копировать
     Public Enumeration ExtensionStage
C++ __Копировать
     public enum class ExtensionStage
F# __Копировать
     type ExtensionStage
##  __Члены
Initialize| 0|  Расширение выполняется при инициализации цепочки расширений.
Рекомендуется использовать только для платформенных расширений.  
---|---|---  
BeforePlatform| 1|  Расширение выполняется перед платформенными расширениями.
Рекомендуется использовать для пользовательских расширений.  
Platform| 2|  Расширение является платформенным и выполняется в середине
цепочки расширений. Рекомендуется использовать только для платформенных
расширений.  
AfterPlatform| 3|  Расширение выполняется после платформенных расширений.
Рекомендуется использовать для пользовательских расширений.  
Finalize| 4|  Расширение выполняется при завершении цепочки расширений.
Рекомендуется использовать только для платформенных расширений.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
