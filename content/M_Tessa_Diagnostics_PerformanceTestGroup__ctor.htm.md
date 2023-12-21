# PerformanceTestGroup(String, Action, Action, Int32, PerformanceTest[]) -
конструктор
Инициализирует новый экземпляр класса
[PerformanceTestGroup](T_Tessa_Diagnostics_PerformanceTestGroup.htm)
##  __Definition
 **Пространство имён:** [Tessa.Diagnostics](N_Tessa_Diagnostics.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PerformanceTestGroup(
    	string name,
    	Action setUp,
    	Action tearDown,
    	int milliseconds,
    	params PerformanceTest[] tests
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	setUp As Action,
    	tearDown As Action,
    	milliseconds As Integer,
    	ParamArray tests As PerformanceTest()
    )
C++ __Копировать
     public:
    PerformanceTestGroup(
    	String^ name, 
    	Action^ setUp, 
    	Action^ tearDown, 
    	int milliseconds, 
    	... array<PerformanceTest^>^ tests
    )
F# __Копировать
     new : 
            name : string * 
            setUp : Action * 
            tearDown : Action * 
            milliseconds : int * 
            tests : PerformanceTest[] -> PerformanceTestGroup
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
setUp [Action](https://learn.microsoft.com/dotnet/api/system.action)
tearDown [Action](https://learn.microsoft.com/dotnet/api/system.action)
milliseconds [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
tests [PerformanceTest](T_Tessa_Diagnostics_PerformanceTest.htm)[]
## __См. также
#### Ссылки
[PerformanceTestGroup - ](T_Tessa_Diagnostics_PerformanceTestGroup.htm)
[PerformanceTestGroup -
перегрузка](Overload_Tessa_Diagnostics_PerformanceTestGroup__ctor.htm)
[Tessa.Diagnostics - пространство имён](N_Tessa_Diagnostics.htm)
