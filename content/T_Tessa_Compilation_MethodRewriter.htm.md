# MethodRewriter - класс
Тип для обхода синтаксического дерева и замена в выбранном методе тела метода
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class MethodRewriter : CSharpSyntaxRewriter
VB __Копировать
     Public Class MethodRewriter
    	Inherits CSharpSyntaxRewriter
C++ __Копировать
     public ref class MethodRewriter : public CSharpSyntaxRewriter
F# __Копировать
     type MethodRewriter = 
        class
            inherit CSharpSyntaxRewriter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CSharpSyntaxVisitor](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxvisitor-1)<[SyntaxNode](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.syntaxnode)> __[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter) __ MethodRewriter
##  __Конструкторы
[MethodRewriter](M_Tessa_Compilation_MethodRewriter__ctor.htm)| Инициализирует
новый экземпляр класса MethodRewriter  
---|---  
##  __Свойства
[VisitIntoStructuredTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitintostructuredtrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitintostructuredtrivia)|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
---|---  
##  __Методы
[DefaultVisit](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxvisitor-1.defaultvisit#microsoft-
codeanalysis-csharp-csharpsyntaxvisitor-1-defaultvisit\(microsoft-
codeanalysis-syntaxnode\))|  
(Унаследован от
[CSharpSyntaxVisitor](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxvisitor-1)<[SyntaxNode](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.syntaxnode)>)  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Visit](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visit#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visit\(microsoft-codeanalysis-
syntaxnode\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAccessorDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitaccessordeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitaccessordeclaration\(microsoft-
codeanalysis-csharp-syntax-accessordeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAccessorList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitaccessorlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitaccessorlist\(microsoft-
codeanalysis-csharp-syntax-accessorlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAliasQualifiedName](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitaliasqualifiedname#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitaliasqualifiedname\(microsoft-
codeanalysis-csharp-syntax-aliasqualifiednamesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAnonymousMethodExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitanonymousmethodexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitanonymousmethodexpression\(microsoft-codeanalysis-csharp-syntax-
anonymousmethodexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAnonymousObjectCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitanonymousobjectcreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitanonymousobjectcreationexpression\(microsoft-codeanalysis-csharp-syntax-
anonymousobjectcreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAnonymousObjectMemberDeclarator](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitanonymousobjectmemberdeclarator#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitanonymousobjectmemberdeclarator\(microsoft-codeanalysis-csharp-syntax-
anonymousobjectmemberdeclaratorsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArgument](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitargument#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitargument\(microsoft-
codeanalysis-csharp-syntax-argumentsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArgumentList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitargumentlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitargumentlist\(microsoft-
codeanalysis-csharp-syntax-argumentlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArrayCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitarraycreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitarraycreationexpression\(microsoft-codeanalysis-csharp-syntax-
arraycreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArrayRankSpecifier](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitarrayrankspecifier#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitarrayrankspecifier\(microsoft-
codeanalysis-csharp-syntax-arrayrankspecifiersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArrayType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitarraytype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitarraytype\(microsoft-
codeanalysis-csharp-syntax-arraytypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitArrowExpressionClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitarrowexpressionclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitarrowexpressionclause\(microsoft-codeanalysis-csharp-syntax-
arrowexpressionclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAssignmentExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitassignmentexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitassignmentexpression\(microsoft-
codeanalysis-csharp-syntax-assignmentexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAttribute](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitattribute#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitattribute\(microsoft-
codeanalysis-csharp-syntax-attributesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAttributeArgument](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitattributeargument#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitattributeargument\(microsoft-
codeanalysis-csharp-syntax-attributeargumentsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAttributeArgumentList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitattributeargumentlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitattributeargumentlist\(microsoft-codeanalysis-csharp-syntax-
attributeargumentlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAttributeList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitattributelist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitattributelist\(microsoft-
codeanalysis-csharp-syntax-attributelistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAttributeTargetSpecifier](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitattributetargetspecifier#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitattributetargetspecifier\(microsoft-codeanalysis-csharp-syntax-
attributetargetspecifiersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitAwaitExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitawaitexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitawaitexpression\(microsoft-
codeanalysis-csharp-syntax-awaitexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBadDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbaddirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbaddirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-baddirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBaseExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbaseexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbaseexpression\(microsoft-
codeanalysis-csharp-syntax-baseexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBaseList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbaselist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbaselist\(microsoft-
codeanalysis-csharp-syntax-baselistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBinaryExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbinaryexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbinaryexpression\(microsoft-
codeanalysis-csharp-syntax-binaryexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBinaryPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbinarypattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbinarypattern\(microsoft-
codeanalysis-csharp-syntax-binarypatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBlock](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitblock#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitblock\(microsoft-codeanalysis-
csharp-syntax-blocksyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBracketedArgumentList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbracketedargumentlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitbracketedargumentlist\(microsoft-codeanalysis-csharp-syntax-
bracketedargumentlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBracketedParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbracketedparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitbracketedparameterlist\(microsoft-codeanalysis-csharp-syntax-
bracketedparameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitBreakStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitbreakstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitbreakstatement\(microsoft-
codeanalysis-csharp-syntax-breakstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCasePatternSwitchLabel](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcasepatternswitchlabel#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitcasepatternswitchlabel\(microsoft-codeanalysis-csharp-syntax-
casepatternswitchlabelsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCaseSwitchLabel](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcaseswitchlabel#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcaseswitchlabel\(microsoft-
codeanalysis-csharp-syntax-caseswitchlabelsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCastExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcastexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcastexpression\(microsoft-
codeanalysis-csharp-syntax-castexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCatchClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcatchclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcatchclause\(microsoft-
codeanalysis-csharp-syntax-catchclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCatchDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcatchdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcatchdeclaration\(microsoft-
codeanalysis-csharp-syntax-catchdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCatchFilterClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcatchfilterclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcatchfilterclause\(microsoft-
codeanalysis-csharp-syntax-catchfilterclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCheckedExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcheckedexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcheckedexpression\(microsoft-
codeanalysis-csharp-syntax-checkedexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCheckedStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcheckedstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcheckedstatement\(microsoft-
codeanalysis-csharp-syntax-checkedstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitClassDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitclassdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitclassdeclaration\(microsoft-
codeanalysis-csharp-syntax-classdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitClassOrStructConstraint](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitclassorstructconstraint#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitclassorstructconstraint\(microsoft-codeanalysis-csharp-syntax-
classorstructconstraintsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCompilationUnit](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcompilationunit#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcompilationunit\(microsoft-
codeanalysis-csharp-syntax-compilationunitsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConditionalAccessExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconditionalaccessexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconditionalaccessexpression\(microsoft-codeanalysis-csharp-syntax-
conditionalaccessexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConditionalExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconditionalexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconditionalexpression\(microsoft-codeanalysis-csharp-syntax-
conditionalexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConstantPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconstantpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitconstantpattern\(microsoft-
codeanalysis-csharp-syntax-constantpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConstructorConstraint](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconstructorconstraint#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconstructorconstraint\(microsoft-codeanalysis-csharp-syntax-
constructorconstraintsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConstructorDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconstructordeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconstructordeclaration\(microsoft-codeanalysis-csharp-syntax-
constructordeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConstructorInitializer](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconstructorinitializer#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconstructorinitializer\(microsoft-codeanalysis-csharp-syntax-
constructorinitializersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitContinueStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcontinuestatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcontinuestatement\(microsoft-
codeanalysis-csharp-syntax-continuestatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConversionOperatorDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconversionoperatordeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconversionoperatordeclaration\(microsoft-codeanalysis-csharp-syntax-
conversionoperatordeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitConversionOperatorMemberCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitconversionoperatormembercref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitconversionoperatormembercref\(microsoft-codeanalysis-csharp-syntax-
conversionoperatormembercrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCrefBracketedParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcrefbracketedparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitcrefbracketedparameterlist\(microsoft-codeanalysis-csharp-syntax-
crefbracketedparameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCrefParameter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcrefparameter#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcrefparameter\(microsoft-
codeanalysis-csharp-syntax-crefparametersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitCrefParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitcrefparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitcrefparameterlist\(microsoft-
codeanalysis-csharp-syntax-crefparameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDeclarationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdeclarationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitdeclarationexpression\(microsoft-codeanalysis-csharp-syntax-
declarationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDeclarationPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdeclarationpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdeclarationpattern\(microsoft-
codeanalysis-csharp-syntax-declarationpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDefaultConstraint](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdefaultconstraint#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdefaultconstraint\(microsoft-
codeanalysis-csharp-syntax-defaultconstraintsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDefaultExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdefaultexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdefaultexpression\(microsoft-
codeanalysis-csharp-syntax-defaultexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDefaultSwitchLabel](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdefaultswitchlabel#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdefaultswitchlabel\(microsoft-
codeanalysis-csharp-syntax-defaultswitchlabelsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDefineDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdefinedirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitdefinedirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
definedirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDelegateDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdelegatedeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdelegatedeclaration\(microsoft-
codeanalysis-csharp-syntax-delegatedeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDestructorDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdestructordeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitdestructordeclaration\(microsoft-codeanalysis-csharp-syntax-
destructordeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDiscardDesignation](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdiscarddesignation#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdiscarddesignation\(microsoft-
codeanalysis-csharp-syntax-discarddesignationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDiscardPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdiscardpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdiscardpattern\(microsoft-
codeanalysis-csharp-syntax-discardpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDocumentationCommentTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdocumentationcommenttrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitdocumentationcommenttrivia\(microsoft-codeanalysis-csharp-syntax-
documentationcommenttriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitDoStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitdostatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitdostatement\(microsoft-
codeanalysis-csharp-syntax-dostatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitElementAccessExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitelementaccessexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitelementaccessexpression\(microsoft-codeanalysis-csharp-syntax-
elementaccessexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitElementBindingExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitelementbindingexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitelementbindingexpression\(microsoft-codeanalysis-csharp-syntax-
elementbindingexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitElifDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitelifdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitelifdirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-elifdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitElseClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitelseclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitelseclause\(microsoft-
codeanalysis-csharp-syntax-elseclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitElseDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitelsedirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitelsedirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-elsedirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEmptyStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitemptystatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitemptystatement\(microsoft-
codeanalysis-csharp-syntax-emptystatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEndIfDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitendifdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitendifdirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-endifdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEndRegionDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitendregiondirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitendregiondirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
endregiondirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEnumDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitenumdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitenumdeclaration\(microsoft-
codeanalysis-csharp-syntax-enumdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEnumMemberDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitenummemberdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitenummemberdeclaration\(microsoft-codeanalysis-csharp-syntax-
enummemberdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEqualsValueClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitequalsvalueclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitequalsvalueclause\(microsoft-
codeanalysis-csharp-syntax-equalsvalueclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitErrorDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visiterrordirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visiterrordirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-errordirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEventDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visiteventdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visiteventdeclaration\(microsoft-
codeanalysis-csharp-syntax-eventdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitEventFieldDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visiteventfielddeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visiteventfielddeclaration\(microsoft-codeanalysis-csharp-syntax-
eventfielddeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitExplicitInterfaceSpecifier](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitexplicitinterfacespecifier#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitexplicitinterfacespecifier\(microsoft-codeanalysis-csharp-syntax-
explicitinterfacespecifiersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitExpressionColon](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitexpressioncolon#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitexpressioncolon\(microsoft-
codeanalysis-csharp-syntax-expressioncolonsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitExpressionStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitexpressionstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitexpressionstatement\(microsoft-
codeanalysis-csharp-syntax-expressionstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitExternAliasDirective](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitexternaliasdirective#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitexternaliasdirective\(microsoft-
codeanalysis-csharp-syntax-externaliasdirectivesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFieldDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfielddeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitfielddeclaration\(microsoft-
codeanalysis-csharp-syntax-fielddeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFileScopedNamespaceDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfilescopednamespacedeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfilescopednamespacedeclaration\(microsoft-codeanalysis-csharp-syntax-
filescopednamespacedeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFinallyClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfinallyclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitfinallyclause\(microsoft-
codeanalysis-csharp-syntax-finallyclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFixedStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfixedstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitfixedstatement\(microsoft-
codeanalysis-csharp-syntax-fixedstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitForEachStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitforeachstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitforeachstatement\(microsoft-
codeanalysis-csharp-syntax-foreachstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitForEachVariableStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitforeachvariablestatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitforeachvariablestatement\(microsoft-codeanalysis-csharp-syntax-
foreachvariablestatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitForStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitforstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitforstatement\(microsoft-
codeanalysis-csharp-syntax-forstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFromClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfromclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitfromclause\(microsoft-
codeanalysis-csharp-syntax-fromclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerCallingConvention](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointercallingconvention#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfunctionpointercallingconvention\(microsoft-codeanalysis-csharp-syntax-
functionpointercallingconventionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerParameter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointerparameter#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfunctionpointerparameter\(microsoft-codeanalysis-csharp-syntax-
functionpointerparametersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointerparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfunctionpointerparameterlist\(microsoft-codeanalysis-csharp-syntax-
functionpointerparameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointertype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitfunctionpointertype\(microsoft-
codeanalysis-csharp-syntax-functionpointertypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerUnmanagedCallingConvention](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointerunmanagedcallingconvention#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfunctionpointerunmanagedcallingconvention\(microsoft-codeanalysis-csharp-
syntax-functionpointerunmanagedcallingconventionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitFunctionPointerUnmanagedCallingConventionList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitfunctionpointerunmanagedcallingconventionlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitfunctionpointerunmanagedcallingconventionlist\(microsoft-codeanalysis-
csharp-syntax-functionpointerunmanagedcallingconventionlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitGenericName](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitgenericname#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitgenericname\(microsoft-
codeanalysis-csharp-syntax-genericnamesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitGlobalStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitglobalstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitglobalstatement\(microsoft-
codeanalysis-csharp-syntax-globalstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitGotoStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitgotostatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitgotostatement\(microsoft-
codeanalysis-csharp-syntax-gotostatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitGroupClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitgroupclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitgroupclause\(microsoft-
codeanalysis-csharp-syntax-groupclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIdentifierName](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitidentifiername#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitidentifiername\(microsoft-
codeanalysis-csharp-syntax-identifiernamesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIfDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitifdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitifdirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-ifdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIfStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitifstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitifstatement\(microsoft-
codeanalysis-csharp-syntax-ifstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitImplicitArrayCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitimplicitarraycreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitimplicitarraycreationexpression\(microsoft-codeanalysis-csharp-syntax-
implicitarraycreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitImplicitElementAccess](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitimplicitelementaccess#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitimplicitelementaccess\(microsoft-codeanalysis-csharp-syntax-
implicitelementaccesssyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitImplicitObjectCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitimplicitobjectcreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitimplicitobjectcreationexpression\(microsoft-codeanalysis-csharp-syntax-
implicitobjectcreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitImplicitStackAllocArrayCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitimplicitstackallocarraycreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitimplicitstackallocarraycreationexpression\(microsoft-codeanalysis-csharp-
syntax-implicitstackallocarraycreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIncompleteMember](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitincompletemember#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitincompletemember\(microsoft-
codeanalysis-csharp-syntax-incompletemembersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIndexerDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitindexerdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitindexerdeclaration\(microsoft-
codeanalysis-csharp-syntax-indexerdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIndexerMemberCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitindexermembercref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitindexermembercref\(microsoft-
codeanalysis-csharp-syntax-indexermembercrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInitializerExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinitializerexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitinitializerexpression\(microsoft-codeanalysis-csharp-syntax-
initializerexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterfaceDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterfacedeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitinterfacedeclaration\(microsoft-
codeanalysis-csharp-syntax-interfacedeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterpolatedStringExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterpolatedstringexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitinterpolatedstringexpression\(microsoft-codeanalysis-csharp-syntax-
interpolatedstringexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterpolatedStringText](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterpolatedstringtext#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitinterpolatedstringtext\(microsoft-codeanalysis-csharp-syntax-
interpolatedstringtextsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterpolation](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterpolation#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitinterpolation\(microsoft-
codeanalysis-csharp-syntax-interpolationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterpolationAlignmentClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterpolationalignmentclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitinterpolationalignmentclause\(microsoft-codeanalysis-csharp-syntax-
interpolationalignmentclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInterpolationFormatClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinterpolationformatclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitinterpolationformatclause\(microsoft-codeanalysis-csharp-syntax-
interpolationformatclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitInvocationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitinvocationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitinvocationexpression\(microsoft-
codeanalysis-csharp-syntax-invocationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitIsPatternExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitispatternexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitispatternexpression\(microsoft-
codeanalysis-csharp-syntax-ispatternexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitJoinClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitjoinclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitjoinclause\(microsoft-
codeanalysis-csharp-syntax-joinclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitJoinIntoClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitjoinintoclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitjoinintoclause\(microsoft-
codeanalysis-csharp-syntax-joinintoclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLabeledStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlabeledstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlabeledstatement\(microsoft-
codeanalysis-csharp-syntax-labeledstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLetClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitletclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitletclause\(microsoft-
codeanalysis-csharp-syntax-letclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLineDirectivePosition](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlinedirectiveposition#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitlinedirectiveposition\(microsoft-codeanalysis-csharp-syntax-
linedirectivepositionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLineDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlinedirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlinedirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-linedirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLineSpanDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlinespandirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitlinespandirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
linespandirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitList(SyntaxTokenList)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlist\(microsoft-codeanalysis-
syntaxtokenlist\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitList(SyntaxTriviaList)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlist\(microsoft-codeanalysis-
syntaxtrivialist\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitList``1(SeparatedSyntaxList<UMP>)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlist-1\(microsoft-codeanalysis-
separatedsyntaxlist\(\(-0\)\)\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitList``1(SyntaxList<UMP>)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlist-1\(microsoft-codeanalysis-
syntaxlist\(\(-0\)\)\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitListElement(SyntaxTrivia)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlistelement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlistelement\(microsoft-
codeanalysis-syntaxtrivia\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitListElement``1(UMP)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlistelement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlistelement-1\(-0\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitListSeparator](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlistseparator#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlistseparator\(microsoft-
codeanalysis-syntaxtoken\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLiteralExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitliteralexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitliteralexpression\(microsoft-
codeanalysis-csharp-syntax-literalexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLoadDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitloaddirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitloaddirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-loaddirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLocalDeclarationStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlocaldeclarationstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitlocaldeclarationstatement\(microsoft-codeanalysis-csharp-syntax-
localdeclarationstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLocalFunctionStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlocalfunctionstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitlocalfunctionstatement\(microsoft-codeanalysis-csharp-syntax-
localfunctionstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitLockStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitlockstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitlockstatement\(microsoft-
codeanalysis-csharp-syntax-lockstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitMakeRefExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitmakerefexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitmakerefexpression\(microsoft-
codeanalysis-csharp-syntax-makerefexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitMemberAccessExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitmemberaccessexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitmemberaccessexpression\(microsoft-codeanalysis-csharp-syntax-
memberaccessexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitMemberBindingExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitmemberbindingexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitmemberbindingexpression\(microsoft-codeanalysis-csharp-syntax-
memberbindingexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitMethodDeclaration](M_Tessa_Compilation_MethodRewriter_VisitMethodDeclaration.htm)|  
(Переопределяет
[CSharpSyntaxRewriter.VisitMethodDeclaration(MethodDeclarationSyntax)](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitmethoddeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitmethoddeclaration\(microsoft-
codeanalysis-csharp-syntax-methoddeclarationsyntax\)))  
[VisitNameColon](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnamecolon#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitnamecolon\(microsoft-
codeanalysis-csharp-syntax-namecolonsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitNameEquals](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnameequals#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitnameequals\(microsoft-
codeanalysis-csharp-syntax-nameequalssyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitNameMemberCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnamemembercref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitnamemembercref\(microsoft-
codeanalysis-csharp-syntax-namemembercrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitNamespaceDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnamespacedeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitnamespacedeclaration\(microsoft-
codeanalysis-csharp-syntax-namespacedeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitNullableDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnullabledirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitnullabledirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
nullabledirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitNullableType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitnullabletype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitnullabletype\(microsoft-
codeanalysis-csharp-syntax-nullabletypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitObjectCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitobjectcreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitobjectcreationexpression\(microsoft-codeanalysis-csharp-syntax-
objectcreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOmittedArraySizeExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitomittedarraysizeexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitomittedarraysizeexpression\(microsoft-codeanalysis-csharp-syntax-
omittedarraysizeexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOmittedTypeArgument](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitomittedtypeargument#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitomittedtypeargument\(microsoft-
codeanalysis-csharp-syntax-omittedtypeargumentsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOperatorDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitoperatordeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitoperatordeclaration\(microsoft-
codeanalysis-csharp-syntax-operatordeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOperatorMemberCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitoperatormembercref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitoperatormembercref\(microsoft-
codeanalysis-csharp-syntax-operatormembercrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOrderByClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitorderbyclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitorderbyclause\(microsoft-
codeanalysis-csharp-syntax-orderbyclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitOrdering](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitordering#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitordering\(microsoft-
codeanalysis-csharp-syntax-orderingsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParameter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparameter#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitparameter\(microsoft-
codeanalysis-csharp-syntax-parametersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitparameterlist\(microsoft-
codeanalysis-csharp-syntax-parameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParenthesizedExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparenthesizedexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitparenthesizedexpression\(microsoft-codeanalysis-csharp-syntax-
parenthesizedexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParenthesizedLambdaExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparenthesizedlambdaexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitparenthesizedlambdaexpression\(microsoft-codeanalysis-csharp-syntax-
parenthesizedlambdaexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParenthesizedPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparenthesizedpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitparenthesizedpattern\(microsoft-
codeanalysis-csharp-syntax-parenthesizedpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitParenthesizedVariableDesignation](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitparenthesizedvariabledesignation#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitparenthesizedvariabledesignation\(microsoft-codeanalysis-csharp-syntax-
parenthesizedvariabledesignationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPointerType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpointertype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitpointertype\(microsoft-
codeanalysis-csharp-syntax-pointertypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPositionalPatternClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpositionalpatternclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitpositionalpatternclause\(microsoft-codeanalysis-csharp-syntax-
positionalpatternclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPostfixUnaryExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpostfixunaryexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitpostfixunaryexpression\(microsoft-codeanalysis-csharp-syntax-
postfixunaryexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPragmaChecksumDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpragmachecksumdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitpragmachecksumdirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
pragmachecksumdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPragmaWarningDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpragmawarningdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitpragmawarningdirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
pragmawarningdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPredefinedType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpredefinedtype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitpredefinedtype\(microsoft-
codeanalysis-csharp-syntax-predefinedtypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPrefixUnaryExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitprefixunaryexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitprefixunaryexpression\(microsoft-codeanalysis-csharp-syntax-
prefixunaryexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPrimaryConstructorBaseType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitprimaryconstructorbasetype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitprimaryconstructorbasetype\(microsoft-codeanalysis-csharp-syntax-
primaryconstructorbasetypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPropertyDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpropertydeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitpropertydeclaration\(microsoft-
codeanalysis-csharp-syntax-propertydeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitPropertyPatternClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitpropertypatternclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitpropertypatternclause\(microsoft-codeanalysis-csharp-syntax-
propertypatternclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitQualifiedCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitqualifiedcref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitqualifiedcref\(microsoft-
codeanalysis-csharp-syntax-qualifiedcrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitQualifiedName](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitqualifiedname#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitqualifiedname\(microsoft-
codeanalysis-csharp-syntax-qualifiednamesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitQueryBody](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitquerybody#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitquerybody\(microsoft-
codeanalysis-csharp-syntax-querybodysyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitQueryContinuation](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitquerycontinuation#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitquerycontinuation\(microsoft-
codeanalysis-csharp-syntax-querycontinuationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitQueryExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitqueryexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitqueryexpression\(microsoft-
codeanalysis-csharp-syntax-queryexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRangeExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrangeexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrangeexpression\(microsoft-
codeanalysis-csharp-syntax-rangeexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRecordDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrecorddeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrecorddeclaration\(microsoft-
codeanalysis-csharp-syntax-recorddeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRecursivePattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrecursivepattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrecursivepattern\(microsoft-
codeanalysis-csharp-syntax-recursivepatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitReferenceDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitreferencedirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitreferencedirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
referencedirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRefExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrefexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrefexpression\(microsoft-
codeanalysis-csharp-syntax-refexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRefType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitreftype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitreftype\(microsoft-codeanalysis-
csharp-syntax-reftypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRefTypeExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitreftypeexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitreftypeexpression\(microsoft-
codeanalysis-csharp-syntax-reftypeexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRefValueExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrefvalueexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrefvalueexpression\(microsoft-
codeanalysis-csharp-syntax-refvalueexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRegionDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitregiondirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitregiondirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
regiondirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitRelationalPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitrelationalpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitrelationalpattern\(microsoft-
codeanalysis-csharp-syntax-relationalpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitReturnStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitreturnstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitreturnstatement\(microsoft-
codeanalysis-csharp-syntax-returnstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSelectClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitselectclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitselectclause\(microsoft-
codeanalysis-csharp-syntax-selectclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitShebangDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitshebangdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitshebangdirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
shebangdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSimpleBaseType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitsimplebasetype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitsimplebasetype\(microsoft-
codeanalysis-csharp-syntax-simplebasetypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSimpleLambdaExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitsimplelambdaexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitsimplelambdaexpression\(microsoft-codeanalysis-csharp-syntax-
simplelambdaexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSingleVariableDesignation](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitsinglevariabledesignation#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitsinglevariabledesignation\(microsoft-codeanalysis-csharp-syntax-
singlevariabledesignationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSizeOfExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitsizeofexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitsizeofexpression\(microsoft-
codeanalysis-csharp-syntax-sizeofexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSkippedTokensTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitskippedtokenstrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitskippedtokenstrivia\(microsoft-
codeanalysis-csharp-syntax-skippedtokenstriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitStackAllocArrayCreationExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitstackallocarraycreationexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitstackallocarraycreationexpression\(microsoft-codeanalysis-csharp-syntax-
stackallocarraycreationexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitStructDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitstructdeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitstructdeclaration\(microsoft-
codeanalysis-csharp-syntax-structdeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSubpattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitsubpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitsubpattern\(microsoft-
codeanalysis-csharp-syntax-subpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSwitchExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitswitchexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitswitchexpression\(microsoft-
codeanalysis-csharp-syntax-switchexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSwitchExpressionArm](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitswitchexpressionarm#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitswitchexpressionarm\(microsoft-
codeanalysis-csharp-syntax-switchexpressionarmsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSwitchSection](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitswitchsection#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitswitchsection\(microsoft-
codeanalysis-csharp-syntax-switchsectionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitSwitchStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitswitchstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitswitchstatement\(microsoft-
codeanalysis-csharp-syntax-switchstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitThisExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitthisexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitthisexpression\(microsoft-
codeanalysis-csharp-syntax-thisexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitThrowExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitthrowexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitthrowexpression\(microsoft-
codeanalysis-csharp-syntax-throwexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitThrowStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitthrowstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitthrowstatement\(microsoft-
codeanalysis-csharp-syntax-throwstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitToken](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittoken#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittoken\(microsoft-codeanalysis-
syntaxtoken\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittrivia\(microsoft-codeanalysis-
syntaxtrivia\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTryStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittrystatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittrystatement\(microsoft-
codeanalysis-csharp-syntax-trystatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTupleElement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittupleelement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittupleelement\(microsoft-
codeanalysis-csharp-syntax-tupleelementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTupleExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittupleexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittupleexpression\(microsoft-
codeanalysis-csharp-syntax-tupleexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTupleType](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittupletype#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittupletype\(microsoft-
codeanalysis-csharp-syntax-tupletypesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeArgumentList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeargumentlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypeargumentlist\(microsoft-
codeanalysis-csharp-syntax-typeargumentlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeConstraint](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeconstraint#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypeconstraint\(microsoft-
codeanalysis-csharp-syntax-typeconstraintsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeCref](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypecref#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypecref\(microsoft-
codeanalysis-csharp-syntax-typecrefsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeOfExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeofexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypeofexpression\(microsoft-
codeanalysis-csharp-syntax-typeofexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeParameter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeparameter#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypeparameter\(microsoft-
codeanalysis-csharp-syntax-typeparametersyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeParameterConstraintClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeparameterconstraintclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visittypeparameterconstraintclause\(microsoft-codeanalysis-csharp-syntax-
typeparameterconstraintclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypeParameterList](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypeparameterlist#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypeparameterlist\(microsoft-
codeanalysis-csharp-syntax-typeparameterlistsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitTypePattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visittypepattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visittypepattern\(microsoft-
codeanalysis-csharp-syntax-typepatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitUnaryPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitunarypattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitunarypattern\(microsoft-
codeanalysis-csharp-syntax-unarypatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitUndefDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitundefdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitundefdirectivetrivia\(microsoft-
codeanalysis-csharp-syntax-undefdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitUnsafeStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitunsafestatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitunsafestatement\(microsoft-
codeanalysis-csharp-syntax-unsafestatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitUsingDirective](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitusingdirective#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitusingdirective\(microsoft-
codeanalysis-csharp-syntax-usingdirectivesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitUsingStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitusingstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitusingstatement\(microsoft-
codeanalysis-csharp-syntax-usingstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitVariableDeclaration](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitvariabledeclaration#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitvariabledeclaration\(microsoft-
codeanalysis-csharp-syntax-variabledeclarationsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitVariableDeclarator](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitvariabledeclarator#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitvariabledeclarator\(microsoft-
codeanalysis-csharp-syntax-variabledeclaratorsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitVarPattern](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitvarpattern#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitvarpattern\(microsoft-
codeanalysis-csharp-syntax-varpatternsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitWarningDirectiveTrivia](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitwarningdirectivetrivia#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitwarningdirectivetrivia\(microsoft-codeanalysis-csharp-syntax-
warningdirectivetriviasyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitWhenClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitwhenclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitwhenclause\(microsoft-
codeanalysis-csharp-syntax-whenclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitWhereClause](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitwhereclause#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitwhereclause\(microsoft-
codeanalysis-csharp-syntax-whereclausesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitWhileStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitwhilestatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitwhilestatement\(microsoft-
codeanalysis-csharp-syntax-whilestatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitWithExpression](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitwithexpression#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitwithexpression\(microsoft-
codeanalysis-csharp-syntax-withexpressionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlCDataSection](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlcdatasection#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlcdatasection\(microsoft-
codeanalysis-csharp-syntax-xmlcdatasectionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlComment](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlcomment#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlcomment\(microsoft-
codeanalysis-csharp-syntax-xmlcommentsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlCrefAttribute](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlcrefattribute#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlcrefattribute\(microsoft-
codeanalysis-csharp-syntax-xmlcrefattributesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlElement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlelement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlelement\(microsoft-
codeanalysis-csharp-syntax-xmlelementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlElementEndTag](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlelementendtag#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlelementendtag\(microsoft-
codeanalysis-csharp-syntax-xmlelementendtagsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlElementStartTag](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlelementstarttag#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlelementstarttag\(microsoft-
codeanalysis-csharp-syntax-xmlelementstarttagsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlEmptyElement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlemptyelement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlemptyelement\(microsoft-
codeanalysis-csharp-syntax-xmlemptyelementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlName](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlname#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlname\(microsoft-codeanalysis-
csharp-syntax-xmlnamesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlNameAttribute](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlnameattribute#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlnameattribute\(microsoft-
codeanalysis-csharp-syntax-xmlnameattributesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlPrefix](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlprefix#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmlprefix\(microsoft-
codeanalysis-csharp-syntax-xmlprefixsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlProcessingInstruction](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmlprocessinginstruction#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-
visitxmlprocessinginstruction\(microsoft-codeanalysis-csharp-syntax-
xmlprocessinginstructionsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlText](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmltext#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmltext\(microsoft-codeanalysis-
csharp-syntax-xmltextsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitXmlTextAttribute](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visitxmltextattribute#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visitxmltextattribute\(microsoft-
codeanalysis-csharp-syntax-xmltextattributesyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
[VisitYieldStatement](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter.visityieldstatement#microsoft-
codeanalysis-csharp-csharpsyntaxrewriter-visityieldstatement\(microsoft-
codeanalysis-csharp-syntax-yieldstatementsyntax\))|  
(Унаследован от
[CSharpSyntaxRewriter](https://learn.microsoft.com/dotnet/api/microsoft.codeanalysis.csharp.csharpsyntaxrewriter))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
