# PlaceholderCompiler - конструктор
Инициализирует новый экземпляр класса
[PlaceholderCompiler](T_Tessa_Compilation_Placeholders_PlaceholderCompiler.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Placeholders](N_Tessa_Compilation_Placeholders.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public PlaceholderCompiler(
    	ICompiler compiler,
    	ICompilationSourceProvider sourceProvider,
    	[DependencyAttribute("PlaceholderPreprocessor")] IPreprocessor preprocessor
    )
VB __Копировать
     Public Sub New ( 
    	compiler As ICompiler,
    	sourceProvider As ICompilationSourceProvider,
    	<DependencyAttribute("PlaceholderPreprocessor")> preprocessor As IPreprocessor
    )
C++ __Копировать
     public:
    PlaceholderCompiler(
    	ICompiler^ compiler, 
    	ICompilationSourceProvider^ sourceProvider, 
    	[DependencyAttribute(L"PlaceholderPreprocessor")] IPreprocessor^ preprocessor
    )
F# __Копировать
     new : 
            compiler : ICompiler * 
            sourceProvider : ICompilationSourceProvider * 
            [<DependencyAttribute("PlaceholderPreprocessor")>] preprocessor : IPreprocessor -> PlaceholderCompiler
#### Параметры
compiler [ICompiler](T_Tessa_Compilation_ICompiler.htm)
sourceProvider
[ICompilationSourceProvider](T_Tessa_Compilation_ICompilationSourceProvider.htm)
preprocessor [IPreprocessor](T_Tessa_Compilation_IPreprocessor.htm)
## __См. также
#### Ссылки
[PlaceholderCompiler -
](T_Tessa_Compilation_Placeholders_PlaceholderCompiler.htm)
[Tessa.Compilation.Placeholders - пространство
имён](N_Tessa_Compilation_Placeholders.htm)
