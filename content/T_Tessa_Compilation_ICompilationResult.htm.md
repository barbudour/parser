# ICompilationResult - интерфейс
Результат компиляции.
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICompilationResult
VB __Копировать
     Public Interface ICompilationResult
C++ __Копировать
     public interface class ICompilationResult
F# __Копировать
     type ICompilationResult = interface end
##  __Свойства
[Assembly](P_Tessa_Compilation_ICompilationResult_Assembly.htm)|  Исполняемая
сборка, результат компиляции. В случае неудачной компиляции равно null  
---|---  
[AssemblyBytes](P_Tessa_Compilation_ICompilationResult_AssemblyBytes.htm)|  
[AssemblyID](P_Tessa_Compilation_ICompilationResult_AssemblyID.htm)|
Уникальный идентификатор сборки  
[BuildDate](P_Tessa_Compilation_ICompilationResult_BuildDate.htm)|  Дата
сборки версии платформы, при которой выполнялась компиляция  
[BuildVersion](P_Tessa_Compilation_ICompilationResult_BuildVersion.htm)|
Версия платформы, при которой выполнялась компиляция  
[CompilationDateTime](P_Tessa_Compilation_ICompilationResult_CompilationDateTime.htm)|
Дата/время сборки  
[CompilerOutput](P_Tessa_Compilation_ICompilationResult_CompilerOutput.htm)|
Вывод компилятора  
[CompilerReturnValue](P_Tessa_Compilation_ICompilationResult_CompilerReturnValue.htm)|
Возвращаемое значение процесса компилятора  
[Info](P_Tessa_Compilation_ICompilationResult_Info.htm)|  Дополнительная
информация  
[RawOutput](P_Tessa_Compilation_ICompilationResult_RawOutput.htm)|
Неформатированный вывод компилятора  
[ValidationResult](P_Tessa_Compilation_ICompilationResult_ValidationResult.htm)|
Ошибки и предупреждения выполненной сборки  
## __Методы расширения
[Resolve<T>](M_Tessa_Compilation_CompilationExtensions_Resolve__1.htm)|  Найти
в результате сборки тип, реализующий интерфейс T и создать его экземпляр В
случае отсутствия хотя бы одного типа в сборке будет выброшено
System.InvalidOperationException  
(Определяется
[CompilationExtensions](T_Tessa_Compilation_CompilationExtensions.htm))  
---|---  
[ResolveAll<T>](M_Tessa_Compilation_CompilationExtensions_ResolveAll__1.htm)|
Найти в результате сборки все типы, реализующие интерфейс T и создать их
экземпляры  
(Определяется
[CompilationExtensions](T_Tessa_Compilation_CompilationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
