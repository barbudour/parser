# ICompilationSourceBuilder - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICompilationSourceBuilder
VB __Копировать
     Public Interface ICompilationSourceBuilder
C++ __Копировать
     public interface class ICompilationSourceBuilder
F# __Копировать
     type ICompilationSourceBuilder = interface end
##  __Свойства
[Length](P_Tessa_Compilation_ICompilationSourceBuilder_Length.htm)|  Текущая
длина строки без учета пространств имен, добавленных через
[ICompilationSourceBuilder.Length].  
---|---  
## __Методы
[AddUsings(IEnumerable<String>)](M_Tessa_Compilation_ICompilationSourceBuilder_AddUsings.htm)|
Добавить конструкцию using _namespace; в начало  
---|---  
[AddUsings(String)](M_Tessa_Compilation_ICompilationSourceBuilder_AddUsings_1.htm)|
Добавить конструкцию using _namespace; в начало  
[AddUsings(String[])](M_Tessa_Compilation_ICompilationSourceBuilder_AddUsings_2.htm)|
Добавить конструкцию using _namespace; в начало  
[Append(IEnumerable<String>)](M_Tessa_Compilation_ICompilationSourceBuilder_Append.htm)|
Добавить конструкцию using _namespace; в начало  
[Append(String)](M_Tessa_Compilation_ICompilationSourceBuilder_Append_1.htm)|
Добавить участок кода в конец.  
[Append(String[])](M_Tessa_Compilation_ICompilationSourceBuilder_Append_2.htm)|
Добавить конструкцию using _namespace; в начало  
[AppendLine(IEnumerable<String>)](M_Tessa_Compilation_ICompilationSourceBuilder_AppendLine.htm)|
Добавить строки кода в конец.  
[AppendLine(String)](M_Tessa_Compilation_ICompilationSourceBuilder_AppendLine_1.htm)|
Добавить строку кода в конец  
[AppendLine(String[])](M_Tessa_Compilation_ICompilationSourceBuilder_AppendLine_2.htm)|
Добавить строки кода в конец.  
[Build](M_Tessa_Compilation_ICompilationSourceBuilder_Build.htm)|  Выполнить
построение исходного кода. Все пространства имен будут помещены в начало с
конструкицей using  
[SetID](M_Tessa_Compilation_ICompilationSourceBuilder_SetID.htm)|  Установить
идентификатор исходного кода.  
[SetName](M_Tessa_Compilation_ICompilationSourceBuilder_SetName.htm)|
Установить имя для конструируемых исходных кодов.  
##  __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
